const API_BASE = "http://localhost:8000";

function el(id) {
  return document.getElementById(id);
}

function formatPrice(value) {
  if (value === null || value === undefined) return "N/A";
  try {
    return new Intl.NumberFormat("en-US").format(value) + " EUR";
  } catch {
    return String(value) + " EUR";
  }
}

function escapeHtml(text) {
  return String(text ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function listingCard(item) {
  const address = escapeHtml(item.address || "Unknown address");
  const price = formatPrice(item.price_in_euro);
  const meta = [
    item.property_type ? escapeHtml(item.property_type) : null,
    item.sqm ? `${item.sqm} sqm` : null,
    item.bedrooms != null ? `${item.bedrooms} bed` : null,
    item.bathrooms != null ? `${item.bathrooms} bath` : null,
  ].filter(Boolean).join(" • ");

  return `
    <a class="card" href="./listing.html?id=${encodeURIComponent(item.id)}">
      <div class="card-title">${address}</div>
      <div class="card-price">${escapeHtml(price)}</div>
      <div class="card-meta">${escapeHtml(meta)}</div>
    </a>
  `;
}

async function loadListings() {
  const status = el("status");
  const container = el("listings");

  const q = el("q")?.value?.trim() || "";
  const limit = Number(el("limit")?.value || 20);

  const url = new URL(`${API_BASE}/listings`);
  url.searchParams.set("limit", String(isNaN(limit) ? 20 : limit));
  if (q) url.searchParams.set("q", q);

  status.textContent = "Loading...";
  container.innerHTML = "";

  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const data = await res.json(); // fetch() + response.json() pattern [web:383]
    const items = data.items || [];

    status.textContent = `Showing ${items.length} of ${data.total ?? items.length} results`;

    if (items.length === 0) {
      container.innerHTML = `<div class="muted">No results.</div>`;
      return;
    }

    container.innerHTML = items.map(listingCard).join("");
  } catch (err) {
    status.textContent = "Error loading data";
    container.innerHTML = `<div class="error">Could not load listings. Is the API running on ${API_BASE}?</div>`;
    console.error(err);
  }
}

function main() {
  const apiBaseText = el("apiBaseText");
  if (apiBaseText) apiBaseText.textContent = API_BASE;

  const form = el("filters");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      loadListings();
    });
  }

  loadListings();
}

main();
