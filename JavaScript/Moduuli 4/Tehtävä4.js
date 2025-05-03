const form = document.getElementById('search-form');
const resultContainer = document.getElementById('results');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const query = document.getElementById('query').value;

  try {
    const response = await fetch(
        `https://api.tvmaze.com/search/shows?q=${query}`);
    const data = await response.json();

    resultContainer.innerHTML = '';

    data.forEach(tvShow => {
      const show = tvShow.show;

      const article = document.createElement('article');

      const showName = document.createElement('h2');
      showName.textContent = showName.name;
      article.appendChild(showName);

      const showUrl = document.createElement('a');
      showUrl.href = show.url;
      showUrl.target = '_blank';
      showUrl.textContent = 'Lisää tietoa';
      article.appendChild(showUrl);

      const showImage = document.createElement('img');
      showImage.src = show.image && show.image.medium ? show.image.medium :
          'https://via.placeholder.com/210x295?text=Not%20Found';
      showImage.alt = show.name;
      article.appendChild(showImage);

      const showSummary = document.createElement('div');
      showSummary.innerHTML = show.summary || 'Ei tiivistelmää saatavilla';
      article.appendChild(showSummary);

      resultContainer.appendChild(article);
    });
  } catch (error) {
    console.log(error.message);
  }
});