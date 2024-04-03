<script>
	import "../app.pcss"
	import Sidebar from '$lib/components/Sidebar.svelte'
</script>

<main class="h-dvh w-[calc(100dvw-5rem)] ml-16">
	<Sidebar />
	<slot />
</main>