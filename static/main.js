           $(document).ready(function () {
            listing();

        });
            var tmp = -1;
            var index = 0;
        function sorting() {
            $.ajax({
                type: 'GET',
                url: '/veggie',
                data: {},
                success: function (response) {
                    let rows = response['veggie']
                    for (let i = 0; i < rows.length; i++) {
                        let likes = rows[i]['likes']
                        if (likes > tmp) {
                            tmp = likes
                            index = i
                        }
                    }

                }
            })
            console.log(index);
            return index
        }

        function listing() {
            let tmp;
            $.ajax({
                type: 'GET',
                url: '/veggie',
                data: {},
                success: function (response) {
                    let rows = response['veggie']
                    for (let i = 0; i < rows.length; i++) {
                        let comment = rows[i]['comment']
                        let title = rows[i]['title']
                        let image = rows[i]['image']
                        let likes = rows[i]['likes']
                        tmp = sorting();


                        if (tmp == i) {
                            let temp_html2 = `<div class="col">
                                            <div class="card h-100">
                                                <img src="${image}"
                                                     class="card-img-top">
                                                <div class="card-body">
                                                    <h5 class="card-title">${title}</h5>
                                                    <p class="mycomment">${comment}</p>
                                                    <button onclick='thumbs_down("${title}")' type="button" class="btn btn-outline-danger">
                                                        <i class="bi bi-hand-thumbs-down"></i>
                                                        으 싫어🤢${likes}
                                                    </button>
                                                </div>
                                            </div>
                                        </div>`
                            $('#cards-box2').append(temp_html2)


                        } else {
                            let temp_html = `<div class="col">
                                            <div class="card h-100">
                                                <img src="${image}"
                                                     class="card-img-top2">
                                                <div class="card-body">
                                                    <h5 class="card-title">${title}</h5>
                                                    <p class="mycomment">${comment}</p>
                                                    <button onclick='thumbs_down("${title}")' type="button" class="btn btn-outline-danger">
                                                        <i class="bi bi-hand-thumbs-down"></i>
                                                        으 싫어🤢${likes}
                                                    </button>
                                                </div>
                                            </div>
                                        </div>`

                            $('#cards-box').append(temp_html)
                        }
                    }
                }
            })
        }

        function posting() {
            let url = $('#url').val()
            let comment = $('#comment').val()
            let title = $('#title').val()

            if (url.replace(/\s| /gi, "").length == 0) {
                alert("주소를 입력해주세요");
                $('#title').focus();
            }

            if (title.replace(/\s| /gi, "").length == 0) {
                alert("이름을 입력해주세요");
                $('#title').focus();
            }

            if (comment.replace(/\s| /gi, "").length == 0) {
                alert("코멘트를 입력해주세요");
                $('#comment').focus();
            }

            $.ajax({
                type: 'POST',
                url: '/veggie',
                data: {url_give: url, comment_give: comment, title_give: title},
                success: function (response) {

                    alert(response['msg'])
                    window.location.reload()
                }
            });
        }

        function open_box() {
            $('#post-box').show()
        }

        function close_box() {
            $('#post-box').hide()
        }

        function thumbs_down(title) {
            $.ajax({
                type: 'POST',
                url: '/veggie/likes',
                data: { title_give: title},
                success: function (response) {
                    alert(response['msg'])
                    window.location.reload()
                }
            });
        }

        // 이 아래로는 새로만든 메뉴버튼의 함수

    const toggleBtn = document.querySelector('.navbar_toggleBtn');
    const menu = document.querySelector('.navbar_menu');
    const icon = document.querySelector('.navbar_icon');

    toggleBtn.addEventListener('click', () => {
        menu.classList.toggle('active');
        icon.classList.toggle('active');
    });

