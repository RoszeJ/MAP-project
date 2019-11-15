const here = {
   id: '6BXh03RYoCpUzHvqwHfT',
   code: '7nuxf6sIr834SbL_Ox7oRw'
};

const map = L.map('map', {
   center: [51.509865, -0.118092],
   zoom: 5,
   layers: [
      Tangram.leafletLayer({
         scene: 'scene.yaml',
         events: {
            click: onMapClick
         }
      })
   ],
   zoomControl: true
});

async function onMapClick() {
   //We will write code in here later...
}
