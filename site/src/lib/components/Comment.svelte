<script lang="ts">
	import { parse } from "marked"
	import DOMPurify from "isomorphic-dompurify"

	const {
		comment,
		addVisible
	}: {
		comment: {
			body: string
			score: number
			link: string
		}
		addVisible: () => void
	} = $props()

	let div: HTMLDivElement

	$effect(() => {
		const observer = new IntersectionObserver(async e => {
			for (const entry of e) if (!entry.isIntersecting) return
			addVisible()
		})

		observer.observe(div)
		return () => observer.disconnect()
	})
</script>

<div class="flex gap-3">
	<div class="w-12">
		<a href={comment.link} target="_blank" rel="noopener noreferrer">
			<small>Link</small>
		</a>
		<p class="text-red-7 pt-2">
			{comment.score}
		</p>
	</div>
	<div
		bind:this={div}
		class="w-full whitespace-pre-wrap bg-white p-2 px-3 rounded-1 shadow-inner shadow-black/30">
		{#await parse(comment.body)}
			Loading...
		{:then body}
			{@html DOMPurify.sanitize(body, {
				USE_PROFILES: { html: true }
			})}
		{/await}
	</div>
</div>
