<script>
  // import { agentState } from "$lib/store";
  import { API_BASE_URL } from "$lib/api";
  import { onMount } from 'svelte';
  import { website } from "$lib/store";
  // A local variable to hold the iframe src URL.
  let iframeSrc;
  console.log("###############################")
  console.log($website)

  // Use onMount to ensure DOM manipulation happens after the component is mounted
  onMount(() => {
    // This function will now run in the client-side context where 'document' is defined
    const unsubscribe = website.subscribe(value => {
      iframeSrc = value;
      console.log(iframeSrc);
      // Optionally force the iframe to reload if needed
      const iframe = document.getElementById('website-iframe');
      if (iframe) iframe.src = value;
    });

    // Cleanup subscription when the component is destroyed
    return () => {
      unsubscribe();
    };
  });


</script>

<div class="flex flex-col bg-white shadow-lg rounded-xl flex-1 overflow-hidden">
  <div class="p-2 flex items-center border-b" style="background-color:#393939;">
    <div class="flex space-x-2 ml-2 mr-4">
      <div class="w-3 h-3 bg-red-500 rounded-full"></div>
      <div class="w-3 h-3 bg-yellow-400 rounded-full"></div>
      <div class="w-3 h-3 bg-green-500 rounded-full"></div>
    </div>
    <span id="terminal-title" class="text-xs text-white">website</span>
    <!-- <input
      type="text"
      id="browser-url"
      class="flex-grow bg-slate-900 p-2 rounded"
      placeholder="chrome://newtab"
      value={$agentState?.browser_session.url || ""}
      readonly
    /> -->

  </div>
  <div id="browser-content" class="flex-grow overflow-auto">
    <iframe id="website-iframe" src={iframeSrc} style="width: 100%; height: 100%; border: none;"></iframe>
  <!-- </div> -->
    <!-- <iframe src={website} style="width: 100%; height: 100%; border: none;"></iframe> -->
    <!-- <div>  -->
      <!-- <iframe src="https://eclatparis.com/"></iframe> -->

        <!-- Data will be loaded here by HTMX -->
   <!-- </div> -->
    <!-- {#if $agentState?.browser_session.screenshot}
      <img
        class="browser-img"
        src={API_BASE_URL + "/api/get-browser-snapshot?snapshot_path=" + $agentState?.browser_session.screenshot}
        alt="Browser snapshot"
      />
    {:else}
      <div class="text-white text-center mt-5"><strong>💡 TIP:</strong> You can include a Git URL in your prompt to clone a repo!</div>
    {/if} -->
  </div>
</div>

<style>
  #browser-url {
    pointer-events: none
  }

  .browser-img {
    display: block;
    object-fit: contain;
    max-width: 100%;
  }
</style>