import data from "../../static/oneupmanshipRaw.tsv?raw"
import { tsvParse } from "d3"

let inSecondThread = false
const parsed = await Promise.all(
	tsvParse(data).map(async v => {
		if (v.id === "sab2o6") inSecondThread = true
		return {
			body: v.body.replaceAll("¬n", "\n").replaceAll("¬m", "\n"),
			author: v.author,
			timestamp: new Date(+v.timestamp * 1000),
			id: v.id,
			score: +v.score,
		}
	})
)

export const userCommentCount: {
	[key: string]: number
} = parsed.reduce(
	(acc, c) => {
		acc[c.author] = (acc[c.author] || 0) + 1
		return acc
	},
	{} as { [key: string]: number }
)

export const commentsPerUser: {
	[key: string]: string[]
} = parsed.reduce(
	(acc, c) => {
		acc[c.author] = (acc[c.author] || []).concat(c.body)
		return acc
	},
	{} as { [key: string]: string[] }
)

export const userQuotes: {
	[k: string]: [string, string?]
} = {
	HelioDex: [
		"I'm not a robot",
		"https://reddit.com/r/oneupmanship/comments/pfvval/comment/hb736f8",
	],
	amazingpikachu_38: ["{:}"],
	Vlajd: [
		"420 upmanship",
		"https://www.reddit.com/r/AskReddit/comments/os4u1w/comment/h6ookse/",
	],
	"Dijit-Datez": ["Statistics King"],
	"Trial-Name": ["r\\counting"],
	arthursadultdiaper: [
		"One up manship",
		"https://www.reddit.com/r/AskReddit/comments/os4u1w/comment/h6m6nps",
	],
}
