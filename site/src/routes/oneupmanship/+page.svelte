<script lang="ts">
	import randomColour from "$lib/rand"
	import { userCommentCount, commentsPerUser } from "$lib/data"
	import Chart from "$lib/components/Chart.svelte"

	const data: [string, number][] = Object.entries(userCommentCount)
		.sort((a, b) => b[1] - a[1])
		.filter((_, i) => i < 25)

	let currentUser = $state("")
</script>

<Chart
	type="bar"
	data={{
		labels: data.map(e => e[0]),
		datasets: [
			{
				label: "Coments",
				data: data.map(e => e[1]),
				backgroundColor: data.map((_, i) => randomColour(data[i][0]))
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
				type: "logarithmic"
			}
		},
		responsive: false
	}}
	plugins={[
		{
			id: "event-handler",
			beforeEvent: function (chart, args, options) {
				const event = args.event
				if (event.type === "click" && event.native) {
					const element = chart.getElementsAtEventForMode(
						event.native,
						"nearest",
						{ intersect: true },
						false
					)
					const index = element[0]?.index
					if (index === undefined) return // dynamic typing trap
					const label = chart.data.labels?.[index] as string
					currentUser = label
				}
			}
		}
	]} />

<div class="w-250">
	{#if currentUser}
		<h2 class="text-2xl mt-4">Comments by {currentUser}</h2>
		<ul class="flex flex-col gap-3">
			{#each commentsPerUser[currentUser] as comment}
				<li
					class="whitespace-pre-wrap bg-white p-2 px-3 rounded-1 shadow-inner shadow-black/30"
				>{@html comment}</li>
			{/each}
		</ul>
	{/if}
</div>
