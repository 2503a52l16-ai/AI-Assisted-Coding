const form = document.getElementById("registrationForm");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const phone = document.getElementById("phone").value.trim();
  const dept = document.getElementById("dept").value;
  const event = document.getElementById("event").value;

  // Name validation
  if (name.length < 3) {
    alert("Name must be at least 3 characters long.");
    return;
  }

  // Email format validation
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailPattern.test(email)) {
    alert("Please enter a valid email address.");
    return;
  }

  // Phone number validation
  if (!/^\d{10}$/.test(phone)) {
    alert("Phone number must be exactly 10 digits.");
    return;
  }

  // Department and Event validation
  if (dept === "" || event === "") {
    alert("Please select both department and event.");
    return;
  }

  // Success message
  alert(`✅ Registration successful!\n\nThank you, ${name}, for registering for ${event}.`);
  form.reset();
});
