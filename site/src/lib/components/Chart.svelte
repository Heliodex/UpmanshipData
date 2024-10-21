<script lang="ts">
	import {
		Chart,
		registerables,
		type ChartConfiguration,
		type ChartTypeRegistry
	} from "chart.js"

	let {
		type,
		data,
		options,
		plugins,
		loading = $bindable()
	}: ChartConfiguration<keyof ChartTypeRegistry, unknown, unknown> & {
		loading: boolean
	} = $props()

	Chart.register(...registerables)
	Chart.defaults.font.family = "Lexend Deca"
	Chart.defaults.font.size = 14
	Chart.defaults.font.lineHeight = 1

	// check media query colour scheme

	let canvas: HTMLCanvasElement

	$effect(() => {
		const lightTheme = window.matchMedia(
			"(prefers-color-scheme: light)"
		).matches
		Chart.defaults.color = lightTheme ? "black" : "white"
		Chart.defaults.scale.grid.color = lightTheme ? "#0002" : "#fff2"

		new Chart(canvas, { type, data, options, plugins })
		loading = false
	})
</script>

<div class={type == "pie" ? "w-2/3 mx-auto pt-4 pb-6" : "pt-2 pb-4"}>
	<canvas bind:this={canvas} height="200"></canvas>
</div>
