// script.js - Interactive features for Mubarak's digital CV

document.addEventListener('DOMContentLoaded', () => {
  // Initialize Lucide icons
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }

  // --- Terminal Simulator ---
  const terminalInput = document.getElementById('terminal-input');
  const terminalBody = document.getElementById('terminal-body');
  
  const welcomeText = `MUBARAK SECUR SYSTEM [Version 1.0.8]
(c) 2026 MubarakSec Corporation. All rights reserved.

Type 'help' to see the list of available commands.
guest@mubaraksec:~$ `;

  // Initialize terminal output
  const welcomeLines = welcomeText.split('\n');
  let currentWelcomeLineIndex = 0;
  
  function typeWelcomeText() {
    if (currentWelcomeLineIndex < welcomeLines.length) {
      const p = document.createElement('div');
      p.className = 'terminal-output';
      p.textContent = welcomeLines[currentWelcomeLineIndex];
      // Insert before input line
      terminalBody.insertBefore(p, terminalBody.lastElementChild);
      currentWelcomeLineIndex++;
      terminalBody.scrollTop = terminalBody.scrollHeight;
      setTimeout(typeWelcomeText, 60);
    }
  }
  
  // Start welcome text typing
  setTimeout(typeWelcomeText, 200);

  const commands = {
    help: 'Available commands:\n  help      - Show this manual\n  about     - Brief background summary\n  skills    - List core competencies & technical stack\n  projects  - Highlighted tools & projects\n  certs     - List active certifications\n  contact   - Get contact links and options\n  clear     - Clear the terminal console',
    about: 'Mubarak Walid Al-Hammadi\nBachelor of Science in Cybersecurity (Expected 2028)\nEmirates International University\n\nAnalytical and driven cybersecurity student with hands-on experience in\ndeveloping custom security tools, vulnerability discovery, and application analysis.',
    skills: 'Technical Skills & Tools:\n  - Security: Burp Suite, Nmap, Metasploit, Netcat, Playwright\n  - Languages: Python, TypeScript, C++, Bash, JavaScript, Node.js, HTML/CSS, PHP\n  - Competencies: Vulnerability Discovery, Dynamic Instrumentation, Static Analysis,\n                 Web/Mobile Security, Penetration Testing\n  - Languages: Arabic (Native), English (B2)',
    projects: 'Highlighted Projects:\n  - reconnV2    : Autonomous CLI-first web vulnerability discovery tool.\n  - Aegis Mobile : Android application security toolkit combining static & dynamic analysis.\n  - CodeRooms    : Node.js WebSocket collaborative code editor extension.\n  - Find The Five: Educational vulnerability labs in PHP.',
    certs: 'Certifications:\n  - TryHackMe Completed Paths: Jr Penetration Tester, Web Fundamentals, Pre Security, Cyber Security 101\n  - Cisco: Introduction to Cybersecurity, Networking Basics\n  - English: B2 Level Certificate – E-ONE Institute',
    contact: 'Contact Info:\n  - Email: xmobta@gmail.com\n  - Phone: +967 730059208\n  - GitHub: github.com/MubarakSec\n  - LinkedIn: linkedin.com/in/mobta-x-6289193ab\n  - TryHackMe: tryhackme.com/p/mobarkm919'
  };

  terminalInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      const inputVal = terminalInput.value.trim().toLowerCase();
      terminalInput.value = '';
      
      // Output the entered command first
      const userLine = document.createElement('div');
      userLine.className = 'terminal-output';
      userLine.innerHTML = `<span class="terminal-prompt">guest@mubaraksec:~$</span> <span class="terminal-command">${escapeHtml(inputVal)}</span>`;
      terminalBody.insertBefore(userLine, terminalBody.lastElementChild);
      
      if (inputVal === 'clear') {
        // Clear all except the last input element
        const outputs = terminalBody.querySelectorAll('.terminal-output');
        outputs.forEach(el => el.remove());
      } else if (inputVal === '') {
        // Just print prompt
      } else if (commands[inputVal]) {
        const reply = document.createElement('div');
        reply.className = 'terminal-output';
        reply.textContent = commands[inputVal];
        terminalBody.insertBefore(reply, terminalBody.lastElementChild);
      } else {
        const errorReply = document.createElement('div');
        errorReply.className = 'terminal-output';
        errorReply.textContent = `Command '${inputVal}' not found. Type 'help' for available commands.`;
        terminalBody.insertBefore(errorReply, terminalBody.lastElementChild);
      }
      
      terminalBody.scrollTop = terminalBody.scrollHeight;
    }
  });

  // Focus terminal input on clicking anywhere inside terminal body
  document.querySelector('.terminal').addEventListener('click', () => {
    terminalInput.focus();
  });

  function escapeHtml(string) {
    return String(string).replace(/[&<>"']/g, function (s) {
      return {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
      }[s];
    });
  }

  // --- Copy to Clipboard Actions ---
  const copyElements = document.querySelectorAll('.copy-trigger');
  const copyPopup = document.getElementById('copy-popup');
  
  copyElements.forEach(el => {
    el.addEventListener('click', (e) => {
      e.preventDefault();
      const textToCopy = el.getAttribute('data-copy');
      if (textToCopy) {
        navigator.clipboard.writeText(textToCopy).then(() => {
          showCopyNotification(textToCopy);
        });
      }
    });
  });

  function showCopyNotification(text) {
    copyPopup.querySelector('.copied-value').textContent = text;
    copyPopup.classList.add('show');
    setTimeout(() => {
      copyPopup.classList.remove('show');
    }, 2500);
  }

  // --- Smooth Nav Highlight ---
  const sections = document.querySelectorAll('section');
  const navLinks = document.querySelectorAll('.nav-links a');
  
  window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.clientHeight;
      if (pageYOffset >= (sectionTop - 120)) {
        current = section.getAttribute('id');
      }
    });
    
    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href').includes(current)) {
        link.classList.add('active');
      }
    });
  });
});
