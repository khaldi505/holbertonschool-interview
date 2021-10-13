const request = require('request')
const filmId = process.argv[2]
const link = 'https://swapi-api.hbtn.io/api/films/' + filmId


request(link , async function(error, response, body){
  const characters = await JSON.parse(body).characters
  characters.forEach( async (character) => {
  await request(character,  function(err, resp, bd){
    console.log(JSON.parse(bd).name)
  })
  });
});
