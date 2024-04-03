import {
  messages,
  selected,
  projectList,
  website,
} from "./store";

export const API_BASE_URL = "http://127.0.0.1:1337";


export async function fetchProjectList() {
  const response = await fetch(`${API_BASE_URL}/api/project-list`);
  const data = await response.json();
  projectList.set(data.projects);
}

export async function createProject(projectName) {
  await fetch(`${API_BASE_URL}/api/create-project`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ project_name: projectName }),
  });
}

export async function deleteProject(projectName) {
  await fetch(`${API_BASE_URL}/api/delete-project`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ project_name: projectName }),
  });
}

export async function fetchMessages() {
  console.log('fetchMessages')
  const projectName = localStorage.getItem("selectedProject");
  const response = await fetch(`${API_BASE_URL}/api/get-messages`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ project_name: projectName }),
  });
  const data = await response.json();
  messages.set(data);
  // console.log(data)
}

export async function sendMessage(message) {
  console.log('sendMessages')
  const projectName = localStorage.getItem("selectedProject");

  await fetch(`${API_BASE_URL}/api/send-message`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message: message,
      project_name: projectName,
      // base_model: modelId,
    }),
  });
  await fetchMessages();
}

export async function fetchSelected() {
  console.log('fetchSelected')
  const projectName = localStorage.getItem("selectedProject");
  const response = await fetch(`${API_BASE_URL}/api/get-selected`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ project_name: projectName }),
  });
  const data = await response.json();
  selected.set(data);
  console.log(data)
}

export async function selectStore(storename) {
  console.log('selectStore')
  const projectName = localStorage.getItem("selectedProject");

  await fetch(`${API_BASE_URL}/api/select-store`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      store: storename,
      project_name: projectName,
      // base_model: modelId,
    }),
  });
  await fetchSelected();
}

// export async function executeAgent(prompt) {
//   const projectName = localStorage.getItem("selectedProject");
//   const modelId = localStorage.getItem("selectedModel");

//   if (!modelId) {
//     alert("Please select the LLM model first.");
//     return;
//   }

//   await fetch(`${API_BASE_URL}/api/execute-agent`, {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({
//       prompt: prompt,
//       base_model: modelId,
//       project_name: projectName,
//     }),
//   });

//   await fetchMessages();
// }

// export async function getTokenUsage() {
//   const response = await fetch(`${API_BASE_URL}/api/token-usage`);
//   const data = await response.json();
//   return data.token_usage;
// }

export async function fetchBrowserSite(url) {

    const constructedUrl = `${API_BASE_URL}/fetch_external_content?url=${encodeURIComponent(url)}`;

    console.log(constructedUrl);
    // Save the constructed URL in the `website` store
    website.set(constructedUrl);
}

