<div class="flex flex-col w-16 h-full fixed top-0 left-0 z-10 p-4 space-y-3 items-center shadow-2xl justify-between rounded-xl">

  <div class="space-y-3">

    <div class="mt-3 ml-1" style="margin-bottom: 3rem; width: 40px;"> <!-- Directly applying margin-bottom -->
      <!-- <img src="/assets/logo-black.png" alt="Logo" style="width: 120px; height: auto;"> Ensure width and auto height for aspect ratio -->
    </div>

    <div class="p-2 rounded nav-button relative bg-slate-300">
      <button class="text-black flex justify-center w-full">
        🛒 
      </button>
      <span class="tooltip">E-commerce shops</span>
    </div>
    <div class="p-2 rounded nav-button relative">
      <button class="text-black flex justify-center w-full">
        🌍 
      </button>
      <span class="tooltip">Google Map</span>
    </div>
    <div class="p-2 rounded nav-button relative">
      <button class="text-black  flex justify-center w-full">
        🎪
      </button>
      <span class="tooltip">Trade fair</span>
    </div>
    <div class="p-2 rounded nav-button relative">
      <button class="text-black  flex justify-center w-full">
        🛍 
      </button>
      <span class="tooltip">Online Marketplaces</span>
    </div>
  </div>

  <div class="pb-4 rounded nav-button relative">
    <button class="text-black flex justify-center w-full">
      <i class="fas fa-sign-out-alt"></i>
    </button>
    <span class="tooltip">Logout</span>
  </div>

</div>




<style>
  .tooltip {
    visibility: hidden;
    width: 120px;
    background-color: #616161;
    color: #fff;
    text-align: center;
    border-radius: 6px;
    padding: 5px 0;
    position: absolute;
    z-index: 1;
    top: 50%;
    left: 160%;
    transform: translateY(-50%);
    opacity: 0;
    transition: opacity 0.3s;
  }

  .nav-button:hover .tooltip {
    visibility: visible;
    opacity: 1;
  }
</style>
