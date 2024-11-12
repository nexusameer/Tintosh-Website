document.addEventListener("DOMContentLoaded", function () {
  const categoryLinks = document.querySelectorAll(".category-link");
  categoryLinks.forEach((link) => {
    link.addEventListener("click", function (event) {
      event.preventDefault();
      const category = event.target.getAttribute("data-category");
      fetch(`/portfolio/filter/?category=${category}`)
        .then((response) => response.json())
        .then((data) => {
          const portfolioContainer = document.getElementById(
            "portfolio-container"
          );
          portfolioContainer.innerHTML = "";
          data.portfolio.forEach((item) => {
            const div = document.createElement("div");
            div.className =
              "col-md-3 col-sm-6 col-xs-6 filtr-item portfolio-item";
            div.innerHTML = `
                                <div class="portfolio-block">
                                    <img class="img-fluid" src="${item.image_url}" alt="">
                                    <div class="caption">
                                        <a class="search-icon" href="${item.url}" target="_blank">
                                            <i class="tf-ion-ios-search-strong"></i>
                                        </a>
                                        <h4><a href="${item.url}">${item.name}</a></h4>
                                    </div>
                                </div>
                            `;
            portfolioContainer.appendChild(div);
          });
        });
    });
  });
});
