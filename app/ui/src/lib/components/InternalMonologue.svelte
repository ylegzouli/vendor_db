<script>
  import { fetchBrowserSite, selectStore, API_BASE_URL } from "$lib/api";
  import { ClickableTile } from "carbon-components-svelte";
  export let message = {}; // Defaulting to an empty object

  async function handleClick() {
    await fetchBrowserSite(message.url); // Assuming message.url contains the URL to fetch
  }

  function handleSelect() {
    console.log(message.name);
    selectStore(message.name);
  }
</script>

<ClickableTile class="internal-monologue bg-gray-50 p-2 rounded-sm mb-2 flex items-start justify-between space-x-3 w-full"  on:click="{handleClick}">
 <div class="flex items-center">
   <img
     src="{ message.icon }"
     alt="icon"
     class="avatar rounded-full flex-shrink-0 mr-3"
   />
   <div>
     <button class="text-xs font-bold text-black">{message.name}</button>
     <p class="text-sm text-black">{ message.description }</p>
   </div>
 </div>
 <div class="flex gap-2 items-center">
  <button on:click|stopPropagation={handleSelect} class="focus:outline-none">
   <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
     <path stroke="grey" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.5 11.5 11 14l4-4m6 2a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>
   </svg>
  </button>
   <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
     <path stroke="grey" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m15 9-6 6m0-6 6 6m6-3a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>
   </svg>
 </div>
</ClickableTile>

<style>
 .avatar {
   width: 50px;
   height: 50px;
 }
</style>

