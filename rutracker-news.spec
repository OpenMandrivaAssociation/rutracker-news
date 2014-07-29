%bcond_with qt5

Summary:	Rutracker.org new releases fetcher
Name:		rutracker-news
Version:	0.3
Release:	1
License:	GPLv2+
Group:		Networking/News
Url:		http://code.google.com/p/rutracker-news/
# http://rutracker-news.googlecode.com/archive/%{version}.tar.gz
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	imagemagick
%if %{with qt5}
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Widgets)
%else
BuildRequires:	qt4-devel
%endif

%description
Rutracker.org new releases fetcher. Supports most popular subforums (various
movies, TV series, anime etc). Fetches also IMDB ratings where it's possible.
See project homepage for more info.

GUI in Russian only (other languages make no sense for this application).

%files
%doc AUTHORS COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%if %{with qt5}
%qmake_qt5
%else
%qmake_qt4
%endif
%make
for N in 16 32 64 128; do convert %{name}.png -resize ${N}x${N} $N.png; done

%install
install -D %{name} %{buildroot}%{_bindir}/%{name}
install -D 16.png %{buildroot}%{_miconsdir}/%{name}.png
install -D 32.png %{buildroot}%{_liconsdir}/%{name}.png
install -D 64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
install -D 128.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

# menu-entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Rutracker News
Comment=Rutracker.org new releases fetcher
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Qt;Network;News;
EOF

