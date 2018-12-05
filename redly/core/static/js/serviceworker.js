var staticCacheName = 'Redly-v8';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        '/static/imagem/icons/192.png',
        '/static/js/materialize.min.js',
        '/static/js/jquery-3.1.1.min.js',
        '/off/',
        '/static/imagem/icons/256.png',
        '/static/imagem/icons/logo1024.png',
        '/static/sf/SanFranciscoText-Regular.otf',
        '/static/js/node_modules/vue/dist/vue.min.js',
        '/static/js/node_modules/vue-resource/dist/vue-resource.min.js',
        '/static/js/node_modules/jquery/dist/jquery.min.js',
        '/static/js/urlize.js-master/urlize.js',
        '/static/js/urlize.js-master/urlize_tlds.js'
      ]);
    })
  );
});


self.addEventListener('fetch', function(event) {
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
      .catch(() => {
        return caches.match('/off/');
      })
    );
});

function cleanResponse(response) {
    const clonedResponse = response.clone();
    const bodyPromise = 'body' in clonedResponse ? Promise.resolve(clonedResponse.body) : clonedResponse.blob();
    return bodyPromise.then((body) => {
        return new Response(body, {
            headers: clonedResponse.headers,
            status: clonedResponse.status,
            statusText: clonedResponse.statusText,
        });
    });
}
