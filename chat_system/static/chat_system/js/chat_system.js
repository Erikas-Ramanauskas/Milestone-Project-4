window.onload = function() {
      const scrollableElement = document.getElementById('chat-window');
      // Scroll to the bottom of the element
      scrollableElement.scrollTop = scrollableElement.scrollHeight;
};
    
  document.addEventListener("DOMContentLoaded", function() {
    let inputField = document.getElementById('id_content');
    
    if (inputField) {
      inputField.focus();
    }
  });