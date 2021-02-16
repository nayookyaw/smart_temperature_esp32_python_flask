

const articleList = document.getElementById('article-list');
const articleListPagination = document.getElementById('article-list-pagination');
let page = 0;
let count = 10;

addPage(++page);

window.onscroll = function() {
	if (getScrollTop() < getDocumentHeight() - window.innerHeight) return;
	addPage(++page);
};

function fetchPage(page) {
	articleList.appendChild(getArticlePage(page, count));
}

function addPage(page) {
	fetchPage(page);
	// addPaginationPage(page);
}

function getPageId(n) {
	return 'article-page-' + n;
}

function getDocumentHeight() {
	const body = document.body;
	const html = document.documentElement;
	
	return Math.max(
		body.scrollHeight, body.offsetHeight,
		html.clientHeight, html.scrollHeight, html.offsetHeight
	);
};

function getScrollTop() {
	return (window.pageYOffset !== undefined) ? window.pageYOffset : (document.documentElement || document.body.parentNode || document.body).scrollTop;
}

function getArticleImage() {
	const hash = Math.floor(Math.random() * Number.MAX_SAFE_INTEGER);
	const image = new Image;
	image.className = 'article-list__item__image article-list__item__image--loading';

	console.log("testing..");
	// image.src = 'https://myanmar-revolution.s3-ap-southeast-1.amazonaws.com/revolution-images/command_centre_gui2+initial+setting.png';
	
	image.src = 'https://myanmar-revolution.s3-ap-southeast-1.amazonaws.com/revolution-images/2021-02-16-22-12-25erccqgjkuglxdzkhwlbpvgvodenpuh';

	image.onload = function() {
		image.classList.remove('article-list__item__image--loading');
	};
	
	return image;
}

function getArticle() {
	const articleImage = getArticleImage();
	const article = document.createElement('article');
	article.className = 'article-list__item';
	article.appendChild(articleImage);
	
	return article;
}

function getArticlePage(page, articlesPerPage) {
	const pageElement = document.createElement('div');
	pageElement.id = getPageId(page);
	pageElement.className = 'article-list__page';
	
	let offset = 1;
	if (page == 1) { 
		offset = 1 
	} else {
		offset = (count * (page - 1)) + 1
	}

	data = {
		'count' : count,
		'offset' : offset
	}

	$.ajax({
		type: "POST",
		url: $HOST_API + '/get/total/images/count',
		data: data,
		success: function(response) {
			console.log("SUCCESS");
		},
		error: function(err) {
				console.log(err);
		}
	});

	while (articlesPerPage--) {
		pageElement.appendChild(getArticle());
	}
	
	return pageElement;
}

function addPaginationPage(page) {
	const pageLink = document.createElement('a');
	pageLink.href = '#' + getPageId(page);
	pageLink.innerHTML = page;
	
	const listItem = document.createElement('li');
	listItem.className = 'article-list__pagination__item';
	listItem.appendChild(pageLink);
	
	articleListPagination.appendChild(listItem);
	
	if (page === 2) {
		articleListPagination.classList.remove('article-list__pagination--inactive');
	}
}

