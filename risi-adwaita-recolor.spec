Name:           risi-adwaita-recolor
Version:        0.1
Release:        2%{?dist}
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
cp -R adwaita-brown %{buildroot}%{_datadir}/themes/
cp -R adwaita-green %{buildroot}%{_datadir}/themes/
cp -R adwaita-orange %{buildroot}%{_datadir}/themes/
cp -R adwaita-purple %{buildroot}%{_datadir}/themes/
cp -R adwaita-pink %{buildroot}%{_datadir}/themes/
cp -R adwaita-red %{buildroot}%{_datadir}/themes/
cp -R adwaita-brown-dark %{buildroot}%{_datadir}/themes/
cp -R adwaita-green-dark %{buildroot}%{_datadir}/themes/
cp -R adwaita-orange-dark %{buildroot}%{_datadir}/themes/
cp -R adwaita-purple-dark %{buildroot}%{_datadir}/themes/
cp -R adwaita-pink-dark %{buildroot}%{_datadir}/themes/
cp -R adwaita-red-dark %{buildroot}%{_datadir}/themes/

%files
# %license add-license-file-here
# %doc add-docs-here
%{_datadir}/themes/adwaita-brown
%{_datadir}/themes/adwaita-green
%{_datadir}/themes/adwaita-orange
%{_datadir}/themes/adwaita-purple
%{_datadir}/themes/adwaita-pink
%{_datadir}/themes/adwaita-red
%{_datadir}/themes/adwaita-brown-dark
%{_datadir}/themes/adwaita-green-dark
%{_datadir}/themes/adwaita-orange-dark
%{_datadir}/themes/adwaita-purple-dark
%{_datadir}/themes/adwaita-pink-dark
%{_datadir}/themes/adwaita-red-dark
	
%changelog
* Fri Sep 3 2021 PizzaLovingNerd
- First spec file
