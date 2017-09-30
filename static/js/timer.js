(function (){
    'use strict';

    var startTime;
    var timerId;
    var elapsedTime = 0;
    var isRunning = false;
    var isSleeping = false

    var startButton = document.getElementById('start');
    var stopButton = document.getElementById('stop');
    var saveButton = document.getElementById('save');
    var timerText = document.getElementById('timerText');
    //関数の定義////////////////////////////////////////////////

    function setButtonState(start, stop, save) {
        startButton.className = start ? 'btn active' : 'btn inactive';
        stopButton.className = stop ? 'btn active' : 'btn inactive';
        saveButton.className = save ? 'btn active' : 'btn inactive';
    }

    function start_func(){
        if (isRunning) return;
        // ツイート画面を表示
        if (elapsedTime==0){
            $('#studystart').modal('show');
            $('#studystart').on('hidden.bs.modal', function () {
                setButtonState(false, true, false);
                pause_func();
            });
            return;
        } 
    }

    function pause_func(){
        if(isRunning){
            elapsedTime += Date.now() - startTime;
            clearTimeout(timerId);
            setButtonState(false, true, true);
            stopButton.innerHTML = "　再開　";
        }else{
            startTime = Date.now(); // 1970/1/1 00:00:00からの経過ミリ秒
            updateTimerText();
            setButtonState(false, true, false);
            stopButton.innerHTML = "一時停止";
        }
        isRunning = !isRunning;
    }

    function save_func(){
        if(isRunning || elapsedTime==0) return;
        var form = document.getElementById('time-form');
        form.elements['time'].value = parseInt(elapsedTime/1000);
        
        // ツイート画面を表示
        $('#studyend').find('[name=words]').val(time_format_ja(elapsedTime) + " 勉強しました by Study Rival");
        $('#studyend').modal('show');
        $('#studyend').on('hidden.bs.modal', function () {
            document.getElementById('time-form').submit();
        });
    }

    function updateTimerText() {
        timerId = setTimeout(function() {
            var t = Date.now() - startTime + elapsedTime;
            timerText.innerHTML = time_format(t);
            updateTimerText();
        }, 10);
    }

    ////////////////////////////////////////////////////////////

    //ボタンを押した時の処理//////////////////////////////////////
    setButtonState(true, false, false);

    startButton.addEventListener('click', start_func);

    stopButton.addEventListener('click', pause_func);

    saveButton.addEventListener('click', save_func);
    
    $('.tweetform').submit(function(event) {
        var form = $(event.target);
        console.log(form);
        var textbox = form.find('[name=words]');
        var submitbutton = form.find('[type=submit]');
        var csrftoken = form.find('[name=csrfmiddlewaretoken]').val();
        var csrfSafeMethod = function (method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        submitbutton.addClass('inactive');
        $.ajax({
             'url': form.attr('action'),
             'type': 'POST',
             'dataType': 'json',
             'data': {words: textbox.val(), 'csrfmiddlewaretoken': csrftoken},
        }).then(function (data){
                textbox.remove();
                submitbutton.remove();
                form.find('.twitter-icon').attr('src', data['icon']);
                form.find('.twitter-text').text(data['msg']);
                form.find('div.row').show();
                form.find('.modal-title').text("ツイートしました！");
            }, function (){
                submitbutton.removeClass('inactive');
                form.find('.modal-body').append($('<p>').text("ツイートに失敗しました。"));
            }
        );
        return false;
    });
    
    
    //////////////////////////////////////////////////////////

    //バックグラウンド処理を行わないようにする//////////////////
    document.addEventListener("visibilitychange",function(e){
        if(document.hidden){
            if(isRunning){
                isSleeping = true;
                pause_func();
            }
        }else{
            isSleeping = false;
        }
    });
    /////////////////////////////////////////////////////////////

    function time_format(time){
        var zp = function(x){
            return (x<10)?("0"+x):x
        };
        var hr = Math.floor(time/3600000);
        var min = Math.floor(time/60000) % 60;
        var sec = Math.floor(time/1000)%60;
        var ms = Math.floor(time%1000/10);
        return zp(hr)+':'+zp(min)+':'+zp(sec)+'.'+zp(ms); 
    }

    function time_format_ja(time){
        var hr = Math.floor(time/3600000);
        var min = Math.floor(time/60000) % 60;
        var sec = Math.floor(time/1000)%60;
        return hr+'時間'+min+'分'+sec+'秒'; 
    }

})();
