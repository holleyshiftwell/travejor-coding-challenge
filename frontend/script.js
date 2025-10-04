const API_BASE = "http://127.0.0.1:8000"; // adjust if backend runs elsewhere
    const PROFILE_ID = "trav_123"; // change to one of your seeded Firestore profile IDs

    const loadingEl = document.getElementById("loading");
    const errorEl = document.getElementById("error");
    const profileEl = document.getElementById("profile");

    async function loadProfile() {
      try {
        const res = await fetch(`${API_BASE}/profile/${PROFILE_ID}`);
        if (!res.ok) throw new Error("Profile not found");
        const data = await res.json();

        // Fill profile info
        document.getElementById("avatar").src = data.avatarUrl || "https://via.placeholder.com/100";
        document.getElementById("username").textContent = data.username;
        document.getElementById("location").textContent = data.location;
        document.getElementById("bio").textContent = data.bio;
        document.getElementById("editBio").value = data.bio;
        document.getElementById("editInterests").value = data.interests.join(", ");

        const interestsDiv = document.getElementById("interests");
        interestsDiv.innerHTML = "";
        data.interests.forEach(i => {
          const tag = document.createElement("span");
          tag.className = "tag";
          tag.textContent = i;
          interestsDiv.appendChild(tag);
        });

        loadingEl.style.display = "none";
        profileEl.style.display = "block";
      } catch (err) {
        loadingEl.style.display = "none";
        errorEl.style.display = "block";
        errorEl.textContent = "Error: " + err.message;
      }
    }

    async function updateProfile() {
      const newBio = document.getElementById("editBio").value.trim();
      const newInterests = document.getElementById("editInterests").value
        .split(",")
        .map(i => i.trim())
        .filter(i => i);

      const body = {
        bio: newBio,
        interests: newInterests
      };

      try {
        const res = await fetch(`${API_BASE}/profile/${PROFILE_ID}`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(body)
        });

        if (!res.ok) throw new Error("Failed to update profile");
        const data = await res.json();
        alert("Profile updated successfully!");
        loadProfile();
      } catch (err) {
        alert("Error: " + err.message);
      }
    }

    document.getElementById("saveBtn").addEventListener("click", updateProfile);

    loadProfile();