// ─── CACHE VERSION ──────────────────────────────────────────────
const CACHE_NAME = 'case-law-v2';
const urlsToCache = [
  // ── Root / core files ──
  '.',
  'index.html',
  'manifest.json',

  // ── All 21 case files ──
  'cases/terry-v-ohio.html',
  'cases/chimel-v-california.html',
  'cases/arizona-v-gant.html',
  'cases/carroll-v-us.html',
  'cases/whren-v-us.html',
  'cases/wardlow-v-illinois.html',
  'cases/florida-v-jl.html',
  'cases/ny-v-quarles.html',
  'cases/kaupp-v-texas.html',
  'cases/muehler-v-mena.html',
  'cases/horton-v-california.html',
  'cases/minnesota-v-dickerson.html',
  'cases/pennsylvania-v-mimms.html',
  'cases/maryland-v-wilson.html',
  'cases/katz-v-us.html',
  'cases/riley-v-california.html',
  'cases/brigham-city-v-stuart.html',
  'cases/mincey-v-arizona.html',
  'cases/cady-v-dombrowski.html',
  'cases/brown-v-texas.html',
  'cases/res-gestae.html'
];

// ─── INSTALL: cache all assets ──────────────────────────────────
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('[SW] Opened cache');
        return cache.addAll(urlsToCache);
      })
      .catch(err => console.error('[SW] Cache addAll error:', err))
  );
  // Force the waiting service worker to become active
  self.skipWaiting();
});

// ─── ACTIVATE: clean up old caches ─────────────────────────────
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(name => {
          if (name !== CACHE_NAME) {
            console.log('[SW] Deleting old cache:', name);
            return caches.delete(name);
          }
        })
      );
    })
  );
  // Take control of all clients immediately
  self.clients.claim();
});

// ─── FETCH: cache-first, fallback to network ───────────────────
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Cache hit – return the cached version
        if (response) {
          return response;
        }

        // Clone the request because it's a stream
        const fetchRequest = event.request.clone();

        return fetch(fetchRequest)
          .then(response => {
            // Check if we received a valid response
            if (!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }

            // Clone the response because it's a stream
            const responseToCache = response.clone();

            caches.open(CACHE_NAME)
              .then(cache => {
                // Don't cache external resources (e.g., images from other domains)
                // Only cache same-origin requests
                if (event.request.url.startsWith(self.location.origin)) {
                  cache.put(event.request, responseToCache);
                }
              })
              .catch(err => console.warn('[SW] Cache put error:', err));

            return response;
          })
          .catch(() => {
            // Optional: fallback offline page – but we already cached everything
            console.warn('[SW] Fetch failed for:', event.request.url);
            // Return a generic offline response or just let it fail
            return new Response('Offline – please check your connection.', {
              status: 503,
              statusText: 'Service Unavailable'
            });
          });
      })
  );
});