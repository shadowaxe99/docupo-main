const axios = require('axios');
const cheerio = require('cheerio');

const url = 'https://github.com/trending';

axios(url)
  .then(response => {
    const html = response.data;
    const $ = cheerio.load(html);
    const trendingTopics = [];

    $('.Box-row').each(function() {
      const title = $(this).find('h1 > a').text().trim();
      const description = $(this).find('p').text().trim();
      const language = $(this).find('[itemprop=programmingLanguage]').text().trim();
      const stars = $(this).find('.float-sm-right').text().trim();
      const repoUrl = `https://github.com${$(this).find('h1 > a').attr('href')}`;

      axios(repoUrl)
        .then(repoResponse => {
          const repoHtml = repoResponse.data;
          const $ = cheerio.load(repoHtml);
          const contributors = [];

          $('.contrib-person').slice(0, 10).each(function() {
            const contributorName = $(this).find('.css-truncate-target').text().trim();
            contributors.push(contributorName);
          });

          trendingTopics.push({
            title,
            description,
            language,
            stars,
            contributors
          });

          console.log(trendingTopics);
        })
        .catch(console.error);
    });
  })
  .catch(console.error);