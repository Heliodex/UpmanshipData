<script lang="ts">
	import { page } from "$app/stores"
	import { goto } from "$app/navigation"
	import randomColour from "$lib/rand"
	import { userCommentCount, commentsPerUser, userQuotes } from "$lib/data"
	import getAvatar from "$lib/avatar"
	import Chart from "$lib/components/Chart.svelte"
	import Comment from "$lib/components/Comment.svelte"

	const data: [string, number][] = Object.entries(userCommentCount)
		.sort((a, b) => b[1] - a[1])
		.filter((_, i) => i < 25)

	let currentUser = $derived($page.url.searchParams.get("user") || "")
	let commentsVisible = $state(20)
	let chartType = $state<"linear" | "logarithmic">("logarithmic")
	let loading = $state(true)
</script>

<h1 class="pb-6">
	<a
		href="https://reddit.com/r/oneupmanship"
		target="_blank"
		rel="noopener noreferrer">
		r/oneupmanship
	</a>
	statistics
</h1>

{#if loading}
	<p>Loading...</p>
{:else}
	<div class="flex pb-4">
		<h2 class="inline pr-4">Top 25 users by comments</h2>

		<button
			class="bg-blue-5 text-white p-1 px-2 rounded-1 hover:bg-blue-6"
			onclick={() => {
				chartType = chartType === "linear" ? "logarithmic" : "linear"
			}}>
			{#if chartType === "linear"}
				Change to logarithmic
			{:else}
				Change to linear
			{/if}
		</button>
	</div>

	<p>Click a bar to see comments by that user.</p>
{/if}

{#key chartType}
	<Chart
		finishedLoading={() => {
			loading = false
		}}
		type="bar"
		data={{
			labels: data.map(e => e[0]),
			datasets: [
				{
					label: "Coments",
					data: data.map(e => e[1]),
					backgroundColor: data.map((_, i) =>
						randomColour(data[i][0])
					)
				}
			]
		}}
		options={{
			indexAxis: "y",
			plugins: {
				legend: {
					display: false
				}
			},
			scales: {
				x: {
					type: chartType
				}
			}
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

					console.log(currentUser, label)
					if (currentUser === label) goto("?")
					else goto(`?user=${label}`)

					commentsVisible = 20
				}
			}
		]} />
{/key}

{#if !loading && currentUser && typeof currentUser === "string"}
	<div class="flex items-center">
		{#await getAvatar(currentUser)}
			<div class="size-12"></div>
		{:then src}
			<img
				{src}
				alt="{currentUser}'s avatar"
				class="size-12 inline rounded-2" />
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

	<h3>Comments</h3>
	<ul class="flex flex-col gap-3">
		{#key currentUser}
			{#each commentsPerUser[currentUser].slice(0, commentsVisible) as comment}
				<Comment
					{comment}
					addVisible={() => {
						commentsVisible++
					}} />
			{/each}
		{/key}
	</ul>
{/if}
