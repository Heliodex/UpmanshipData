<script lang="ts">
	import "uno.css"
	import "../global.css"

	const { children } = $props()
</script>

<main class="min-h-[calc(100vh-10rem)]">
	{@render children()}
</main>

<footer class="pt-6 pb-2 flex justify-center gap-2">
	<a href="/">stats.heliodex.cf</a>
	|
	<a
		href="https://www.reddit.com/r/oneupmanship/"
		target="_blank"
		rel="noopener noreferrer">
		r/oneupmanship
	</a>
	|
	<a
		href="https://github.com/Heliodex/UpmanshipData/tree/main/site"
		target="_blank"
		rel="noopener noreferrer">
		Source code
	</a>
</footer>
