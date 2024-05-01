<script lang="ts">
	import {
		Chart,
		registerables,
		type ChartConfiguration,
		type ChartTypeRegistry
	} from "chart.js"

	const {
		type,
		data,
		options,
		plugins,
		finishedLoading
	}: ChartConfiguration<keyof ChartTypeRegistry, unknown, unknown> & {
		finishedLoading: () => void
	} = $props()

	Chart.register(...registerables)
	Chart.defaults.font.family = "Lexend"
	Chart.defaults.font.size = 14
	Chart.defaults.font.lineHeight = 1
	Chart.defaults.color = "black"

	let canvas: HTMLCanvasElement

	$effect(() => {
		new Chart(canvas, { type, data, options, plugins })
		finishedLoading()
	})
</script>

<div class="">
	<canvas bind:this={canvas} height="200"></canvas>
</div>
