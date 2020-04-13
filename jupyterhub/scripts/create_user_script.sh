while read user; do
  clear_user="$(echo -e "${user}" | tr -d '[[:space:]]')"
  echo "$clear_user"
  useradd $clear_user
  echo "$clear_user:pp20x5a" | chpasswd
done < user.txt

read -rsp $'Press any key to continue...\n' -n1 key
