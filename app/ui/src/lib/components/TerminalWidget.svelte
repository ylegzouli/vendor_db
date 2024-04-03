<script>
  import { onMount } from "svelte";
  import { DataTable, Button } from "carbon-components-svelte";
  import { selected } from "$lib/store";

  // Define the headers for the DataTable.
  // These should correspond to the keys in the row objects.
  console.log($selected.messages)
  const headers = [
    { key: "name", value: "Name" },
    { key: "description", value: "Description" },
  ];

  $: rows = $selected.messages
    ? $selected.messages.map((message, index) => ({
        id: `row-${index}`,
        name: message.name,
        description: message.description,
      }))
    : [];


</script>

<div class="flex flex-col bg-white shadow-lg rounded-xl flex-1 overflow-hidden">
  <div class="p-2 flex items-center border-b" style="background-color:#393939;">
    <div class="flex space-x-2 ml-2 mr-4">
      <div class="w-3 h-3 bg-red-500 rounded-full"></div>
      <div class="w-3 h-3 bg-yellow-400 rounded-full"></div>
      <div class="w-3 h-3 bg-green-500 rounded-full"></div>
    </div>
    <span id="terminal-title" class="text-xs text-white">Selected leads</span>
  </div>

  <div id="selected-message" class="overflow-y-auto">
    <DataTable
      size="compact"
      {headers}
      {rows}
      sortable={true}
    />
    

  </div>
  <div class="p-2 absolute right-14 bottom-7">
    <Button
      class="rounded-xl w-16"
      kind="secondary"
      size="small"
    >Export</Button>
  </div>
</div>

<style>
  #selected-message::-webkit-scrollbar {
    width: 4px;
  }

  #selected-message::-webkit-scrollbar-track {
    background: #eae9e9;
    border-radius: 10px;
  }

  #selected-message::-webkit-scrollbar-thumb {
    background: #bababb;
    border-radius: 10px;
  }
</style>
