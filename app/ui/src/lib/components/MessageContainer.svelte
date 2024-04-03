<script>
  import { messages } from "$lib/store";
  import { onMount, afterUpdate } from "svelte";
  import InternalMonologue from "$lib/components/InternalMonologue.svelte";

  let messageContainer;
  let previousMessageCount = 0;
  console.log("hehe")
  console.log(messages)

  afterUpdate(() => {
    if ($messages && $messages.length > previousMessageCount) {
      messageContainer.scrollTop = messageContainer.scrollHeight;
      previousMessageCount = $messages.length;
    }
  });
</script>

      
  <div class="internal-monologue shadow-sm rounded-t-xl" style="display: flex; justify-content: space-between; background-color:#393939; align-items: start; padding: 8px; margin-bottom: 8px; ">
    <div>
      {#if $messages.messages && $messages.messages.message && $messages.messages.message.length > 0}
        <div class="ml-2 text-sm text-white">Total: { $messages.messages.message.length } leads</div>
      {:else}
        <div class="ml-2 text-sm text-white">Total: 0 leads</div>
      {/if}
    </div>
    <div style="display: flex; gap: 8px; align-items: center;">
      <p>
        <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
        <path stroke="white" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.5 11.5 11 14l4-4m6 2a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>
      </svg>
      </p>
      <p><svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
        <path stroke="white" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m15 9-6 6m0-6 6 6m6-3a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>
      </svg>
      </p>
    </div>
  </div>
 

<div id="message-container" class="flex-grow overflow-y-auto" bind:this={messageContainer}>
  {#if $messages.messages && $messages.messages.message && $messages.messages.message.length > 0}
  {#each $messages.messages.message as message}
      <InternalMonologue {message} />
  {/each}
{:else}
  <p></p>
  {/if}
</div>

<style>


  #message-container {
    height: 390px;
    overflow-y: auto;
  }

  #message-container::-webkit-scrollbar {
    width: 4px;
  }

  #message-container::-webkit-scrollbar-track {
    background: #eae9e9;
    border-radius: 10px;
  }

  #message-container::-webkit-scrollbar-thumb {
    background: #bababb;
    border-radius: 10px;
  }


</style>