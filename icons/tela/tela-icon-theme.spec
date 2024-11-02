%global _basename tela
%global _version 2024-09-04
%global debug_package %{nil}

Name:               %{_basename}-icon-theme
Version:            1.0.0
Release:            %autorelease
Summary:            Tela icon theme for GNU/Linux
License:            GPL-3.0
URL:                https://github.com/vinceliuice/Tela-icon-theme
Source:             https://github.com/vinceliuice/%{_basename}-icon-theme/archive/refs/tags/%{_version}.tar.gz

BuildArch:          noarch

Requires:           gtk-update-icon-cache

%description
A flat, colorful icon theme

COLOR VARIANTS:

standard    - Standard color folder version
black       - Black color folder version
blue        - Blue color folder version
brown       - Brown color folder version
green       - Green color folder version
grey        - Grey color folder version
orange      - Orange color folder version
pink        - Pink color folder version
purple      - Purple color folder version
red         - Red color folder version
yellow      - yellow color folder version
manjaro     - Manjaro default color folder version
ubuntu      - Ubuntu default color folder version
nord        - Nord color folder version

%prep
%setup -n %{_basename}-%{version}

%build
# Nothing to do here

%install
# Delete useless files from source folder
# rm -f "%{_basename}/create-new-icon-theme.cache.sh"
# rm -f "%{_basename}/icon-theme.cache"
# rm -f "%{_basename}-light/create-new-icon-theme.cache.sh"
# rm -f "%{_basename}-light/icon-theme.cache"
# rm -f "%{_basename}-light-panel/create-new-icon-theme.cache.sh"
# rm -f "%{_basename}-light-panel/icon-theme.cache"
# rm -f "%{_basename}-pgrey/create-new-icon-theme.cache.sh"
# rm -f "%{_basename}-pgrey/icon-theme.cache"

# Install icons
# mkdir -p %{buildroot}%{_datadir}/icons
# cp -dr --no-preserve=mode "%{_basename}" %{buildroot}%{_datadir}/icons/%{_basename}
# cp -dr --no-preserve=mode "%{_basename}-light" %{buildroot}%{_datadir}/icons/%{_basename}-light
# cp -dr --no-preserve=mode "%{_basename}-light-panel" %{buildroot}%{_datadir}/icons/%{_basename}-light-panel
# cp -dr --no-preserve=mode "%{_basename}-pgrey" %{buildroot}%{_datadir}/icons/%{_basename}-pgrey

# export THEMES="%{_basename} %{_basename}-light %{_basename}-light-panel %{_basename}-pgrey"
# for t in $THEMES; do
#     /bin/touch %{buildroot}/%{_datadir}/icons/$t/icon-theme.cache
# done

# # Install license
# mkdir -p %{buildroot}%{_datadir}/licenses/%{name}
# cp -p "LICENSE" %{buildroot}%{_datadir}/licenses/%{name}

%post
# export THEMES="%{_basename} %{_basename}-light %{_basename}-light-panel %{_basename}-pgrey"
# for t in $THEMES; do
#     /bin/touch --no-create %{_datadir}/icons/$t &>/dev/null || :
# done

%postun
# if [ $1 -eq 0 ] ; then
#     export THEMES="%{_basename} %{_basename}-light %{_basename}-light-panel %{_basename}-pgrey"
#     for t in $THEMES; do
#         /bin/touch --no-create %{_datadir}/icons/$t &>/dev/null
#         /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$t &>/dev/null || :
#     done
# fi

%posttrans
# export THEMES="%{_basename} %{_basename}-light %{_basename}-light-panel %{_basename}-pgrey"
# for t in $THEMES; do
#     /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$t &>/dev/null || :
# done

%files
%doc README.md
%license LICENSE
%{_datadir}/icons/%{_basename}
%{_datadir}/icons/%{_basename}-light
%{_datadir}/icons/%{_basename}-light-panel
%{_datadir}/icons/%{_basename}-pgrey

%changelog
%autochangelog