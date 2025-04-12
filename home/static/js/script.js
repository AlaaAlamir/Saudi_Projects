let deleteitem=(id)=>
{
    Swal.fire({
        title: "هل أنت متأكد؟",
        text: "لن تتمكن من استرجاع هذا العنصر بعد الحذف!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        cancelButtonText:"إلغاء",
        confirmButtonText: "نعم, أحذف!"
    }).then((result) => {

        if(result.isConfirmed)
        {
            $.ajax({
                url: 'delete/'+id,
                type:'GET',

                success: function(result)
                {
                    window.location.href='/vision2030'; 
                    Swal.fire({
                        title: "تمت الإزالة!",
                        text: "تم حذف العنصر بنجاح",
                        icon: "success",
                        timer: 1500,
                    });
                }
            });
        }
    });
}