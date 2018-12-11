var staticCacheName = 'redly-v8';
var filesPWA =[
    '/static/imagem/icons/192.png',
    '/static/js/materialize.min.js',
    '/static/js/jquery-3.1.1.min.js',
    '/off/',
    '/static/main.css',
    '/static/main.scss',
    '/static/imagem/icons/256.png',
    '/static/imagem/icons/logo1024.png',
    '/static/sf/SanFranciscoText-Regular.otf',
    '/static/js/node_modules/vue/dist/vue.min.js',
    '/static/js/node_modules/vue-resource/dist/vue-resource.min.js',
    '/static/js/node_modules/jquery/dist/jquery.min.js',
    '/static/js/urlize.js-master/urlize.js',
    '/static/js/urlize.js-master/urlize_tlds.js'
]

self.addEventListener('install', event=> {
  event.waitUntil(
    caches.open(staticCacheName)
        .then(function(cache) {
            return cache.addAll(filesPWA);
        })
  );
});

this.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames
          .filter(cacheName => (cacheName.startsWith('redly-v8')))
          .filter(cacheName => (cacheName !== staticCacheName))
          .map(cacheName => caches.delete(cacheName))
      );
    })
  );
});
self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match('/off/'));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});
// self.addEventListener('fetch', event => {
//   if (event.request.method === 'GET') {
//     let url = event.request.url.indexOf(self.location.origin) !== -1 ?
//       event.request.url.split(`${self.location.origin}/`)[1] :
//       event.request.url;
//     let isFileCached = filesPWA.indexOf(url) !== -1;
//     if (isFileCached) {
//       event.respondWith(
//         caches.open(staticCacheName)
//           .then(cache => {
//             return cache.match(url)
//               .then(response => {
//                 if (response) {
//                   return response;
//                 }
//                 throw Error('There is not response for such request', url);
//               });
//           })
//           .catch(error => {
//             return fetch(event.request);
//           })
//       );
//     }
//   }
// });
