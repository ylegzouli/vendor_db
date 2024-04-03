<script>
  import { onMount } from 'svelte';
  import { projectList } from "$lib/store";
  import { createProject, fetchProjectList, fetchMessages, deleteProject, fetchSelected } from "$lib/api";
  import { Button } from "carbon-components-svelte";
  let selectedProject;

  function selectProject(project) {
    selectedProject = project;
    console.log(project);
    localStorage.setItem("selectedProject", project);
    fetchMessages();
    fetchSelected();
    
  }

  async function createNewProject() {
    const projectName = prompt("Campaign name:");
    if (projectName) {
      await createProject(projectName);
      await fetchProjectList();
      await fetchMessages();
      await fetchSelected();
      selectProject(projectName);
    }
  }

  function setupDropdownToggle(dropdownId, buttonId) {
    const dropdown = document.getElementById(dropdownId);
    const button = document.getElementById(buttonId);

    button.addEventListener('click', function(event) {
      dropdown.classList.toggle('hidden');
      event.stopPropagation(); // Prevent click from immediately bubbling to document
    });
  }

  function setupGlobalClickListener(dropdownId, buttonId) {
    const dropdown = document.getElementById(dropdownId);

    // This listener will close the dropdown if the click is outside
    document.addEventListener('click', function(event) {
      if (!dropdown.contains(event.target) && !event.target.matches(`#${buttonId}, #${buttonId} *`)) {
        dropdown.classList.add('hidden');
      }
    });
  }

  onMount(() => {
    selectedProject = localStorage.getItem("selectedProject") || "Select campagn";

    // Setup dropdown toggles and global click listener for each dropdown
    setupDropdownToggle('project-dropdown', 'project-button');
    setupGlobalClickListener('project-dropdown', 'project-button');
    
    setupDropdownToggle('model-dropdown', 'model-button');
    setupGlobalClickListener('model-dropdown', 'model-button');

    return () => {
      // Clean up global click listener if the component is destroyed
      document.removeEventListener('click', closeDropdowns);
    };
  });

  async function handleDeleteProject(projectName, event) {
    event.preventDefault();
    event.stopPropagation(); // Prevent triggering selectProject
    await deleteProject(projectName);
    // localStorage.setItem("selectedProject", None);
    await fetchProjectList(); // Refresh the list after deletion
  }

</script>

<!-- <div class="control-panel bg-slate-100 border rounded"> -->
  <div class="dropdown-menu relative inline-block rounded-br-xl w-1/2">
    <Button
  
      kind="secondary"

      type="button"
      class=" w-full rounded-bl-xl"
      id="project-button"
      aria-expanded="true"
      aria-haspopup="true"
    >
      <span id="selected-project ">{selectedProject}</span>
      <svg
        class="-mr-1 h-5 w-5 text-white"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
      >
        <path
          fill-rule="evenodd"
          d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z"
          clip-rule="evenodd"
        />
      </svg>
    </Button>

    <div
  id="project-dropdown"
  class="absolute left-0 z-10 mb-2 w-80 origin-bottom-left rounded-md bg-slate-400 shadow-lg ring-1 ring-indigo-700 ring-opacity-5 focus:outline-none hidden"
  style="bottom: 100%;"
  role="menu"
  aria-orientation="vertical"
  aria-labelledby="project-button"
  tabindex="-1"
>
      <div class="py-1" role="none">
        <a
          href="#"
          class="text-white block px-4 py-2 text-sm hover:bg-slate-700"
          on:click|preventDefault={createNewProject}
        >
          + Create new campagn
        </a>
        {#if $projectList !== null}
          {#each $projectList as project}
          <div>
            <a
              href="#"
              class="text-white block px-4 py-2 text-sm hover:bg-slate-700"
              on:click|preventDefault={() => selectProject(project)}
            >
              {project}
            <button
            class="ml-4"
            on:click|preventDefault={(event) => handleDeleteProject(project, event)}
            aria-label="Delete project"
          >
            &#x274C; <!-- This is a simple cross symbol, you can replace it with an SVG or an icon for better visuals -->
          </button>
            </a>
          </div>
          {/each}
        {/if}
      </div>
    </div>
  </div>

<!-- </div> -->

<style>





</style>