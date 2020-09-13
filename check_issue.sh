# Distro should be RHEL, CentOS and Oracle
#__DISTRO=$(grep -ihs "Ubuntu\|SUSE\|Fedora\|Debian\|CentOS\|Red Hat Enterprise Linux\|clear-linux-os\|CoreOS" /{etc,usr/lib}/{issue,*release,*version})
# No long check the distro because of other 3rd parties distro which could have this condition. Omitted distro check part.

# 3.10.0-123 through 3.10.0-693; These are the 7.x kernels.
# 2.6.32-573 through 2.6.32-754; 2.6.32 might be the issued kernel. So we check if it startws with 2.6.32
__kernel_version=$(uname -r)

# LIS version: 4.2.1 through 4.2.4
__lis_version=$(modinfo hv_vmbus | grep ^version: | cut -d ":" -f2| sed -e 's/  */ /g' -e 's/^ *\(.*\) *$/\1/')

# #######################
# fake data
# __kernel_version=3.10.0-125.192
# __lis_version=4.2.3
# #######################

# Main
# increase match_point if a requirement meets in the condition.
match_point=0

# Disto check - optional
# case $__DISTRO in
#     *CentOS*release*7\.*\.*)
#         ((match_point++))
#         ;;
#     *Red*7\.*)
#         ((match_point++))
#         ;;
#     *)
#         echo "not eligible"
#         ;;
# esac
#echo "DISTRO : $match_point"

# lis version check
_lis_ver_mj=$(echo $__lis_version | cut -d "." -f1)
_lis_ver_mn=$(echo $__lis_version | cut -d "." -f2)
_lis_ver_rv=$(echo $__lis_version | cut -d "." -f3)

if [[ $_lis_ver_mj -eq 4 ]]; then
    if [[ $_lis_ver_mn -eq 2 ]]; then
        if [[ $_lis_ver_rv -ge 1 ]] && [[ $_lis_ver_rv -le 4 ]]; then
            ((match_point++))
        fi
    fi
fi

#echo "LIS : $match_point"

# kernel version check
kv1=$(echo $__kernel_version  | cut -d "-" -f1)
kv2=$(echo $__kernel_version  | cut -d "-" -f2 | cut -d '.' -f 1)

if [[ $kv1 == "3.10.0" ]]; then
    if [[ $kv2 -ge 123 ]] && [[ $kv2 -le 693 ]]; then
        ((match_point++))
    fi
fi

if [[ $kv1 == "2.6.32" ]]; then
    ((match_point++))
fi

#echo "KERNEL : $match_point"

if [[ $match_point -eq 2 ]];then
    echo "Your VM falls into the issue criteria. Recommend to follow Microsoft instruction."
else
    echo "Your VM does not fall into the current issue. No further action required."
fi