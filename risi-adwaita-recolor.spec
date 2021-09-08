Name:           risi-adwaita-recolor
Version:        0.1
Release:        3%{?dist}
Summary:        risiOS's accent colors for Adwaita

License:        GPL v3
URL:            risi.io
Source0:        https://github.com/risiOS/Adwaita-recolor/archive/refs/heads/main.tar.gz#/Adwaita-recolor-main.tar.gz

BuildArch:	noarch
Requires:	gtk3
Requires:	gtk4
BuildRequires:	sassc
BuildRequires:	inkscape
BuildRequires:	optipng
BuildRequires:	wget

%description
This is a package with all of risiOS's Adwaita Varients

%prep
%autosetup

%build
bash all-themes.sh

%install
mkdir -p %{buildroot}%{_datadir}/themes
cp -R Adwaita-brown %{buildroot}%{_datadir}/themes/
cp -R Adwaita-green %{buildroot}%{_datadir}/themes/
cp -R Adwaita-orange %{buildroot}%{_datadir}/themes/
cp -R Adwaita-purple %{buildroot}%{_datadir}/themes/
cp -R Adwaita-pink %{buildroot}%{_datadir}/themes/
cp -R Adwaita-red %{buildroot}%{_datadir}/themes/
cp -R Adwaita-brown-dark %{buildroot}%{_datadir}/themes/
cp -R Adwaita-green-dark %{buildroot}%{_datadir}/themes/
cp -R Adwaita-orange-dark %{buildroot}%{_datadir}/themes/
cp -R Adwaita-purple-dark %{buildroot}%{_datadir}/themes/
cp -R Adwaita-pink-dark %{buildroot}%{_datadir}/themes/
cp -R Adwaita-red-dark %{buildroot}%{_datadir}/themes/

%files
# %license add-license-file-here
# %doc add-docs-here
%{_datadir}/themes/Adwaita-brown
%{_datadir}/themes/Adwaita-green
%{_datadir}/themes/Adwaita-orange
%{_datadir}/themes/Adwaita-purple
%{_datadir}/themes/Adwaita-pink
%{_datadir}/themes/Adwaita-red
%{_datadir}/themes/Adwaita-brown-dark
%{_datadir}/themes/Adwaita-green-dark
%{_datadir}/themes/Adwaita-orange-dark
%{_datadir}/themes/Adwaita-purple-dark
%{_datadir}/themes/Adwaita-pink-dark
%{_datadir}/themes/Adwaita-red-dark
	
%changelog
* Fri Sep 3 2021 PizzaLovingNerd
- First spec file
