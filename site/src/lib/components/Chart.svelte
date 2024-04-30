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
		plugins
	}: ChartConfiguration<keyof ChartTypeRegistry, unknown, unknown> = $props()

	Chart.register(...registerables)
	Chart.defaults.font.family = "Lexend"
	Chart.defaults.font.size = 14
	Chart.defaults.font.lineHeight = 1
	Chart.defaults.color = "black"
	// increase bar width

	let canvas: HTMLCanvasElement

	$effect(() => {
		new Chart(canvas, { type, data, options, plugins })
	})
</script>

<div class="w-250">
	<canvas bind:this={canvas} width="1000" height="700"></canvas>
</div>
