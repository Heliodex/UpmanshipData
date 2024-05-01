<script lang="ts">
	import { parse } from "marked"
	import DOMPurify from "isomorphic-dompurify"

	const {
		comment,
		addVisible
	}: {
		comment: string
		addVisible: () => void
	} = $props()

	let li: HTMLLIElement

	$effect(() => {
		const observer = new IntersectionObserver(async e => {
			for (const entry of e) if (!entry.isIntersecting) return
			addVisible()
		})

		observer.observe(li)
		return () => observer.disconnect()
	})
</script>

<li
	bind:this={li}
	class="whitespace-pre-wrap bg-white p-2 px-3 rounded-1 shadow-inner shadow-black/30">
	{#await parse(comment)}
		Loading...
	{:then body}
		{@html DOMPurify.sanitize(body, {
			USE_PROFILES: { html: true }
		})}
	{/await}
</li>
