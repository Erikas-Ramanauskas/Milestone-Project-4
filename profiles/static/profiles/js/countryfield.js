// Function to handle the change event of the select element
function handleCountrySelect() {
  const countrySelect = document.getElementById("id_default_country");

  if (!countrySelect.value) {
    countrySelect.classList.add("empty");
  } else {
    countrySelect.classList.remove("empty");
  }
}

// Adding event listener for change event on the country select
document.getElementById("id_default_country").addEventListener("change", handleCountrySelect);

// Check the initial state on page load
window.addEventListener("load", function () {
  handleCountrySelect();
});
