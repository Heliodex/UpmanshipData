import data from "../../static/oneupmanshipRaw.tsv?raw"
import { tsvParse } from "d3"

let inSecondThread = false
const tsv = tsvParse(data).map(async v => {
	let link: string
	if (v.id === "sab2o6") {
		inSecondThread = true
		link =
			"https://www.reddit.com/r/oneupmanship/comments/sab2o6/original_oneupmanship_post_was_archived_today/"
	} else if (inSecondThread)
		link = `https://www.reddit.com/r/oneupmanship/comments/sab2o6/comment/${v.id}/`
	else
		link = `https://www.reddit.com/r/AskReddit/comments/os4u1w/comment/${v.id}/`

	return {
		body: v.body.replaceAll("¬n", "\n").replaceAll("¬m", "\n"),
		author: v.author,
		timestamp: new Date(+v.timestamp * 1000),
		id: v.id,
		score: +v.score,
		link,
	}
})
const parsed = await Promise.all(tsv)

export const totalComments = parsed.length

export const userCommentCount: {
	[key: string]: number
} = parsed.reduce(
	(acc, c) => {
		acc[c.author] = (acc[c.author] || 0) + 1
		return acc
	},
	{} as { [key: string]: number }
)

export const userUpvoteCount: {
	[key: string]: number
} = parsed.reduce(
	(acc, c) => {
		acc[c.author] = (acc[c.author] || 0) + c.score
		return acc
	},
	{} as { [key: string]: number }
)

type Comments = {
	[key: string]: {
		body: string
		score: number
		link: string
	}[]
}

export const commentsPerUser = parsed.reduce((acc, c) => {
	acc[c.author] = (acc[c.author] || []).concat({
		body: c.body,
		score: c.score,
		link: c.link,
	})
	return acc
}, {} as Comments)

// Number of comments from all users except the top 25
export const othersCount: number = Object.values(userCommentCount)
	.sort((a, b) => b - a)
	.slice(25)
	.reduce((a, b) => a + b, 0)

export const userQuotes: { [k: string]: [string, string?] } = {
	HelioDex: [
		"I'm not a robot",
		"https://reddit.com/r/oneupmanship/comments/pfvval/comment/hb736f8",
	],
	Art_Vandelay_10: [
		"Onward to 69420!",
		"https://www.reddit.com/r/AskReddit/comments/os4u1w/comment/h72ua3z/",
	],
	amazingpikachu_38: ["{:}"],
	Vlajd: [
		"420 upmanship",
		"https://www.reddit.com/r/AskReddit/comments/os4u1w/comment/h6ookse/",
	],
	"Dijit-Datez": ["Statistics King"],
	JackSaysHello: [
		"Hello!",
		"https://www.reddit.com/r/AskReddit/comments/b2qry1/comment/eiuy02c/",
	],
	"Trial-Name": ["r\\counting"],
	arthursadultdiaper: [
		"One up manship",
		"https://www.reddit.com/r/AskReddit/comments/os4u1w/comment/h6m6nps/",
	],
}
