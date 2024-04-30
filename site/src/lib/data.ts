import data from "../../static/oneupmanshipRaw.tsv?raw"
import { tsvParse } from "d3"
import { parse } from "marked"
import DOMPurify from "isomorphic-dompurify"

const parsed = await Promise.all(
	tsvParse(data).map(async v => {
		const body = v.body.replaceAll("¬n", "\n").replaceAll("¬m", "\n")
		return {
			body: DOMPurify.sanitize(await parse(body), {
				USE_PROFILES: { html: true },
			}),
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
