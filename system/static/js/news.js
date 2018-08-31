Vue.component('news', {
    props: ['post'],
    template: '<div class="post-wrapper col-sm-12 col-lg-4">' +
        '<div class="post">' +
        '<h1>{{ post.title }}</h1>' +
        '<img :src="post.image" alt="">' +
        '<p>{{ post.content }}</p>' +
        '</div> ' +
        '</div>',
});

Vue.component('paginator', {
    props: ['page'],
    template: '<button @click="pageClicked(page)" class="btn">{{ page }}</button>',
    methods: {
        pageClicked: function (page) {
            app.changePage(page);
        }
    }
});

var app = new Vue({
    el: '#app',
    data: {
        currentPage: 1,
        maxPages: 1,
        pages: [],
        posts: []
    },
    methods: {
        changePage: function (pageNumber) {
            this.currentPage = pageNumber;
            this.refreshNews();
        },
        refreshNews: function () {
            var request = new XMLHttpRequest();
            request.onreadystatechange = function () {

                if (this.readyState == 4 && this.status == 200) {
                    app.posts = [];
                    var response = JSON.parse(this.responseText);
                    for (post of response.posts) {
                        app.posts.push(post);
                    }
                    app.maxPages = response.pages;
                    app.refreshPages();
                }
            };
            var page = this.currentPage;
            request.open('GET', '/api/?page='+page, true);
            request.send();
        },
        refreshPages: function () {
            this.pages = [];
            for (var counter = 1; counter <=this.maxPages; counter++) {
                this.pages.push(counter);
            }
        }
    }
});

app.refreshNews();
app.refreshPages();
