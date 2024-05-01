import { browser } from "$app/environment"

if (browser) localStorage.setItem("pfpCache", JSON.stringify({}))

const getCache = () =>
	new Map<string, string>(
		Object.entries(JSON.parse(localStorage.getItem("pfpCache") || "{}"))
	)

const setCache = (cache: Map<string, string>) =>
	localStorage.setItem("pfpCache", JSON.stringify(Object.fromEntries(cache)))

export default async (username: string) => {
	if (username === "[deleted]") return ""
	const cache = getCache()
	if (cache.has(username)) return cache.get(username)

	const res = await fetch(
		`https://www.reddit.com/user/${username}/about.json`
	)
	if (res.status === 404) {
		cache.set(username, "")
		setCache(cache)
		return ""
	}
	if (!res.ok) return ""

	const img = (await res.json()).data.icon_img.split("?")[0]
	cache.set(username, img)
	setCache(cache)
	return img
}
