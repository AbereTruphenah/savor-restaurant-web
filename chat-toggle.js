// Grab elements
const toggleBtn = document.getElementById('chat-toggle');
const chatBox  = document.getElementById('chat-section');

/**
 * Toggles the visibility of the chat section
 * by swapping utility classes.
 */
function toggleChat() {
  const open = chatBox.classList.contains('opacity-100');

  if (!open) {
    chatBox.classList.remove('opacity-0', 'scale-95', 'pointer-events-none', 'translate-y-4');
    chatBox.classList.add   ('opacity-100', 'scale-100', 'pointer-events-auto', 'translate-y-0');
  } else {
    chatBox.classList.add   ('opacity-0', 'scale-95', 'pointer-events-none', 'translate-y-4');
    chatBox.classList.remove('opacity-100', 'scale-100', 'pointer-events-auto', 'translate-y-0');
  }
}

// Bind click listener
toggleBtn.addEventListener('click', toggleChat);
