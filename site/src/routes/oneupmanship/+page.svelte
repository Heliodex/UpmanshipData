<script lang="ts">
	import { browser } from "$app/environment"
	import { goto } from "$app/navigation"
	import { page } from "$app/stores"
	import randomColour from "$lib/rand"
	import {
		totalComments,
		userCommentCount,
		commentsPerUser,
		userQuotes,
		othersCount
	} from "$lib/data"
	import getAvatar from "$lib/avatar"
	import Chart from "$lib/components/Chart.svelte"
	import Comment from "$lib/components/Comment.svelte"

	const data: [string, number][] = Object.entries(userCommentCount)
		.sort((a, b) => b[1] - a[1])
		.filter((_, i) => i < 25)

	const labels = data.map(e => e[0]).concat("Others")
	const commentData = data.map(e => e[1]).concat(othersCount)
	const backgroundColours = data
		.map((_, i) => randomColour(data[i][0]))
		.concat("#333")

	let currentUser = $derived(
		browser ? $page.url.searchParams.get("user") || "" : ""
	)
	let commentsVisible = $state(20)
	let chartType = $state<"linear" | "logarithmic" | "pie">("logarithmic")
	let loading = $state(true)

	let sortAsc = $state(true)
	let comments = $derived(
		sortAsc
			? commentsPerUser[currentUser]
			: commentsPerUser[currentUser].slice().reverse()
	)
</script>

<h1>
	<a
		href="https://reddit.com/r/oneupmanship"
		target="_blank"
		rel="noopener noreferrer">
		r/oneupmanship
	</a>
	statistics
</h1>

<p class="pt-2 pb-6">
	{totalComments} total comments &mdash;
	{Object.keys(userCommentCount).length} unique users
</p>

{#if loading}
	<p>Loading...</p>
{:else}
	<div class="flex pb-4">
		<h2 class="inline pr-4">Top 25 users by comments</h2>

		<button
			class="bg-blue-5 text-white p-1 px-2 rounded-1 hover:bg-blue-6"
			onclick={() => {
				if (chartType === "linear") chartType = "logarithmic"
				else if (chartType === "logarithmic") chartType = "pie"
				else chartType = "linear"
			}}>
			{#if chartType === "pie"}
				Change to linear bar
			{:else if chartType === "logarithmic"}
				Change to pie
			{:else}
				Change to logarithmic bar
			{/if}
		</button>
	</div>

	<p class="pb-4">
		Click a {chartType === "pie" ? "segment" : "bar"} on the chart to see comments
		by that user.
	</p>
{/if}

{#key chartType}
	<Chart
		finishedLoading={() => {
			loading = false
		}}
		type={chartType === "pie" ? "pie" : "bar"}
		data={{
			labels: chartType === "pie" ? labels.slice().reverse() : labels,
			datasets: [
				{
					label: "Comments",
					data:
						chartType === "pie"
							? commentData.slice().reverse()
							: commentData,
					backgroundColor:
						chartType === "pie"
							? backgroundColours.slice().reverse()
							: backgroundColours
				}
			]
		}}
		options={{
			indexAxis: "y",
			plugins: { legend: { display: false } },
			scales:
				chartType === "pie"
					? {}
					: {
							x: { type: chartType },
							y: { grid: { color: "transparent" } }
						},
			borderColor: "transparent"
		}}
		plugins={[
			{
				id: "event-handler",
				beforeEvent(chart, args) {
					const event = args.event
					if (!(event.type === "click" && event.native)) return
					const element = chart.getElementsAtEventForMode(
						event.native,
						"nearest",
						{ intersect: true },
						false
					)
					const index = element[0]?.index
					if (index === undefined) return // dynamic typing trap
					const label = chart.data.labels?.[index]?.toString() || ""
					if (label === "Others") return

					goto(currentUser === label ? "?" : `?user=${label}`)

					commentsVisible = 20
				}
			}
		]} />
{/key}

{#if !loading && currentUser && typeof currentUser === "string" && comments}
	<div class="flex items-center">
		{#await getAvatar(currentUser)}
			<div class="size-12"></div>
		{:then src}
			<img
				{src}
				alt="{currentUser}'s avatar"
				class="size-12.5 p-0.5 inline rounded-2 bg-neutral-8 @light:bg-white shadow-inner shadow-black/30" />
		{/await}
		<h2 class="pl-4">
			Statistics for
			<a
				href="https://www.reddit.com/user/{currentUser}/"
				target="_blank"
				rel="noopener noreferrer">
				{currentUser}
			</a>
		</h2>
		{#if userQuotes[currentUser]}
			{@const [quote, href] = userQuotes[currentUser]}
			<i class="ps-2">
				&mdash;
				{#if href}
					<a {href} target="_blank" rel="noopener noreferrer">
						"{quote}"
					</a>
				{:else}
					"{quote}"
				{/if}
			</i>
		{/if}
	</div>

	<div class="py-4">
		<p>{userCommentCount[currentUser]} total comments</p>
	</div>

	<h3 class="flex gap-3 pb-4">
		Comments

		<button
			class="bg-blue-5 text-white p-0.5 px-1.5 rounded-1 hover:bg-blue-6 text-sm"
			onclick={() => {
				commentsVisible = 20
				sortAsc = !sortAsc
			}}>
			Sort by {sortAsc ? "newest" : "oldest"}
		</button>
	</h3>
	<div class="flex flex-col gap-3">
		{#key currentUser}
			{#each comments.slice(0, commentsVisible) as comment}
				<Comment
					{comment}
					addVisible={() => {
						commentsVisible++
					}} />
			{/each}
		{/key}
	</div>
{/if}
