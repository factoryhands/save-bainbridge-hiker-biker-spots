function sendEmail() {
  let emailBody = document.getElementById('email-body').value;
  const nameInput = document.getElementById('name-input');
  const name = nameInput && nameInput.value ? nameInput.value : '';
  const subject = "Save Bike Camping - Email";
  
  if (!emailBody.startsWith('Dear Mr. Banman,')) {
    emailBody = `Dear Mr. Banman,\n\n${emailBody}`;
  }

  let mailtoLink = `mailto:tomb@biparks.org?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(emailBody)}`;

  if (name) {
    mailtoLink += `%0D%0A%0D%0A%0D%0AYours sincerely,%0D%0A${encodeURIComponent(name)}`;
  }

  window.location.href = mailtoLink;
}

window.onload = function() {
  fetch('/generate')
    .then(response => response.json())
    .then(data => typeWriter('email-body', data.text, 0));
}

function typeWriter(elementId, txt, i) {
  if (i < txt.length) {
    document.getElementById(elementId).value += txt.charAt(i);
    setTimeout(function() { typeWriter(elementId, txt, i + 1); }, 10); // Reduced delay to speed up the typewriter effect
  }
}

function fetchNewLetter() {
  fetch('/generate')
    .then(response => response.json())
    .then(data => {
      document.getElementById("email-body").value = '';
      typeWriter("email-body", data.text, 0);
    });
}
