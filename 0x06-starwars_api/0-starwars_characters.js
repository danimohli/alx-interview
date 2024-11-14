#!/usr/bin/env node

const fetch = require('node-fetch');

// Get movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.log("Usage: ./star_wars_characters.js <movie_id>");
  process.exit(1);
}

// Base URL for the Star Wars API
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

async function fetchCharacterNames() {
  try {
    // Fetch movie details
    const filmResponse = await fetch(filmUrl);
    
    if (!filmResponse.ok) {
      throw new Error(`Error fetching movie details: ${filmResponse.statusText}`);
    }
    
    const filmData = await filmResponse.json();
    
    // Fetch each character's name in sequence
    for (const characterUrl of filmData.characters) {
      const characterResponse = await fetch(characterUrl);
      
      if (!characterResponse.ok) {
        throw new Error(`Error fetching character data: ${characterResponse.statusText}`);
      }
      
      const characterData = await characterResponse.json();
      console.log(characterData.name);
    }
  } catch (error) {
    console.error(error.message);
  }
}

fetchCharacterNames();
