function display_alert()
  {
            Swal.fire({
            title: 'Selection has been saved',
            showConfirmButton: true,
            timerProgressBar: true,
            timer:3000,
        });
}

// var name = document.getElementsByName("InputName");
// var ad = document.getElementsByName("InputAd");
// var phone = document.getElementsByName("Inputphone");
// console.log(name);
// console.log(ad);
// console.log(phone);
    // if (beChose<1){
    //     // alert('error...');
    //     Swal.fire({
    //     icon: 'error',
    //     title: 'Oops...',
    //     text: 'Please select at least 1 test case',
    //     timer: 5000,
    //     timerProgressBar: true,
    //     footer:'The page will be re-directed in five seconds'
    //             });
    // }
    // else{
    //     // alert('Success');
    //         Swal.fire({
    //         title: 'Selection has been saved',
    //         showConfirmButton: false,
    //         timerProgressBar: true,
    //         timer:3000,
    //         imageUrl:'/static/img/GearCheck.png'
    //     });}