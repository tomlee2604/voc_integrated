const CACHE_NAME = 'voc-report-v1';
const urlsToCache = [
  '/voc_integrated/',
  '/voc_integrated/index.html',
  '/voc_integrated/manifest.json',
  '/voc_integrated/icon-192.png',
  '/voc_integrated/icon-512.png'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          return response;
        }
        return fetch(event.request);
      }
    )
  );
});</content>
<parameter name="filePath">c:\Users\etland\Desktop\claude\통합 VOC\sw.js