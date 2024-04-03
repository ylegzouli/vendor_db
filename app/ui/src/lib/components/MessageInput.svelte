<script>
  import { sendMessage, API_BASE_URL } from "$lib/api";
  // import { messages } from "$lib/store";
  import { TextArea } from "carbon-components-svelte";
  import ControlPanel from "$lib/components/ControlPanel.svelte";
  import { ButtonSet, Button } from "carbon-components-svelte";



  let messageInput = "";
  async function handleSendMessage() {
    const projectName = localStorage.getItem("selectedProject");

    if (!projectName) {
      alert("Please select a campaign first!");
      return;
    }

    if (messageInput.trim() !== "") {
      console.log("Executing lead search:", messageInput);
      // if ($messages.length === 0) {
      //   // await executeAgent(messageInput);
      // } else {
      //   console.log("Sending message", messageInput);
      await sendMessage(messageInput);
      // }
      messageInput = "";
    }
  }


</script>

<div class="expandable-input w-full">
  <TextArea
    id="message-input"
    class=" shadow-md text-black  text-sm"
    placeholder="Type your lead request.. 
💡 Exemple: Give me 100 jewelry store in Paris and Marseille."
    bind:value={messageInput}
    keydown={(e) => {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        handleSendMessage();
      }
    }}
  ></TextArea>
  <div class="w-full">
  <!-- <ButtonSet class=""> -->
    <ControlPanel />
    <Button
    class="rounded-br-xl w-full shadow-md text-white "   
    id="send-message-btn"
    on:click={handleSendMessage}

  >
    <!-- {@html isAgentActive ? "<i>Agent is busy...</i>" : "Send"} -->
    Find Leads 🔎
  </Button>
  <!-- </ButtonSet> -->
  </div>
</div>

<style>

</style>