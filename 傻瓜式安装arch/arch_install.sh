#!/bin/bash
prompt(){
read -p "$1" back
case $back in
N | n ) exit;;
esac
echo $back
}

prompt "测试网络连接，请插上网线,然后按回车键开始(输入N或n退出)"
dhcpcd

ping -c 4 www.baidu.com
read -p "看看网络是否正常,正常请按回车键继续"
read -p "让看一眼当前的硬盘,按回车键继续(输入N或n退出)" back
fdisk -l

echo "接下来进行分区操作(cfdisk),请自行查看文档,请输入要进行分区的硬盘(a,b,c......),分区一般为 EFI文件系统·Linux swap·Linux FileSystem,请认真观察你想要分区的硬盘(如nvme0n1,sda)"
read -p "请输入你想要分区的硬盘" back
cfdisk /dev/$back

prompt "再看一眼需要分区的硬盘是否已经分好区,按回车键继续(输入N或n退出)"
fdisk -l

read -p "开始对各个分区进行格式化,请输入一个想作为EFI文件系统的分区(输入sd*1,2,3.......)" back
mkfs.fat -F32 /dev/$back

read -p "开始对各个分区进行格式化,请输入一个想作为Linux swap的分区(输入sd*1,2,3.......)" back
mkswap /dev/$back

read -p "开始对各个分区进行格式化,请输入一个想作为Linux FileSyetem的分区(输入sd*1,2,3.......)" back
mkfs.ext4 /dev/$back

read -p "将交换分区初始化,请输入刚才的交换分区(输入sd*1,2,3.......)" back
mkswap /dev/$back

read -p "打开交换分区,请输入交换分区(输入sd*1,2,3.......)" back
swapon /dev/$back

read -p "把刚才的Linux FileSystem分区挂载到/mnt,请输入Linux FileSystem分区(输入sd*1,2,3.......)" back
mount /dev/$back /mnt

read -p "创建一个boot目录,把刚才的EFI文件系统分区挂载到/mnt/boot,请输入EFI分区(输入sd*1,2,3.......)" back
mkdir -p /mnt/boot/efi
mount /dev/$back /mnt/boot/efi

read -p "准备安装基本软件包·Linux内核以及常规硬件的固件,接下来开始换国内源操作(输入:1.阿里源,2.中科大源,3.清华源)" back
case $back in
1)
sed -i '5a Server = http://mirrors.aliyun.com/archlinux/$repo/os/$arch' /etc/pacman.d/mirrorlist;;
2)
sed -i '5a Server = https://mirrors.ustc.edu.cn/archlinux/$repo/os/$arch' /etc/pacman.d/mirrorlist;;
3)
sed -i '5a Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch' /etc/pacman.d/mirrorlist;;
esac

prompt "开始配置arch安装环境,按回车键继续(输入N或n退出)"
pacman -Sy arch-install-scripts

prompt "开始安装基本软件包·Linux内核以及常规硬件的固件,按回车键继续(输入N或n退出)"
pacstrap /mnt base linux linux-firmware vim bash-completion sudo zsh ttf-dejavu wqy-microhei networkmanager sddm sddm-kcm plasma-desktop breeze-gtk kde-gtk-config plasma-pa plasma-nm powerdevil kscreen kgamma5 kinfocenter konsole fcitx-im kcm-fcitx kate dolphin colord-kde gpm ark partitionmanager plasma-systemmonitor kwalletmanager kdeconnect sshfs bluez-utils bluedevil pulseaudio-bluetooth ttf-dejavu wqy-microhei grub efibootmgr
arch-chroot /mnt systemctl enable sddm

prompt "自动挂载分区,按回车键继续(输入N或n退出)"
genfstab -U /mnt >> /mnt/etc/fstab

back=`prompt "设置时区,请输入相应的时区格式如Asia/Shanghai(输入N或n退出)"`
arch-chroot /mnt ln -sf /usr/share/zoneinfo/$back /etc/localtime

prompt "自动对时,按回车键继续(输入N或n退出)"
arch-chroot /mnt hwclock --systohc

prompt "开始进行本地化设置(默认使用简体中文),回车键继续"
arch-chroot /mnt sed -i 's/#zh_CN.U/zh_CN.U/' /etc/locale.gen
arch-chroot /mnt locale-gen
arch-chroot /mnt echo 'LANG=zh_CN.UTF-8' > /mnt/etc/locale.conf

back=`prompt "请输入自己想要的主机名"`
arch-chroot /mnt echo "$back" >> /etc/hostname
arch-chroot /mnt echo -e "127.0.0.1 localhost\n::1 localhost\n127.0.0.1 $back.localdomain $back"

prompt "请输入你想要设置的root密码,回车键开始设置"
arch-chroot /mnt passwd

back=`prompt "如果你是英特尔CPU用户,请输入i;如果是AMD用户请输入a"`
case $back in
i | I ) arch-chroot /mnt pacman -S intel-ucode;;
a | A ) arch-chroot /mnt pacman -S amd-ucode;;
esac

back=`prompt "如果你是英伟达显卡用户,请输入n;如果你是AMD显卡用户(不考虑ATI产品),请输入a;如果你是英特尔显卡用户,请输入i"`
case $back in
n | N ) arch-chroot /mnt pacman -S nvidia nvidia-utils nvidia-prime nvidia-settings;;
a | A ) arch-chroot /mnt pacman -S xf86-video-amdgpu;;
i | I ) arch-chroot /mnt pacman -S xf86-video-intel vulkan-intel;;
esac

back=`prompt "创建一个非root用户,请输入你想要的用户名,输入N或n退出"`
arch-chroot /mnt useradd -G wheel -m $back
arch-chroot /mnt sed -i 's/# %wheel ALL=(ALL:ALL) N/%wheel ALL=(ALL:ALL) N/' /etc/sudoers
echo "请输入你要对该用户设置的密码"
arch-chroot /mnt passwd $back

read -p "是否要安装中文输入法(fcitx5-chewing),是请输入y,否请按回车,结束此脚本请输入n" back
case $back in
y | Y ) arch-chroot /mnt pacman -S fcitx5-chewing;;
n | N ) exit
esac

read -p "是否要安装代理软件(v2raya),是请输入y,否请按回车,结束此脚本请输入n" back
case $back in
y | Y ) arch-chroot /mnt pacman -S v2ray v2raya;;
n | N ) exit
esac

back=`prompt "配置grub启动管理器,输入N或n退出"`
arch-chroot /mnt grub-install
arch-chroot /mnt grub-mkconfig -o /boot/grub/grub.cfg

echo "自此,基本安装已结束(补充:如果进系统后没有监测到音频设备请执行pacman -S sof-firmware alsa-utils pulseaudio-alsa安装音频设备)"
