Name:     ocaml-inotify

Version:  2.3
Release:  1
Summary:  OCaml bindings for inotify
License:  GPLv2+
URL:      https://github.com/whitequark/ocaml-inotify
Source0:  https://github.com/whitequark/ocaml-inotify/archive/v%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamlbuild
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-lwt-devel
BuildRequires: inotify-tools-devel
BuildRequires: ocaml-lwt
Requires:      inotify-tools

%prep
%setup -q

%build
./configure \
   --prefix=%{_prefix} \
   --docdir=%{buildroot}/%{_prefix}/share/doc
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
/usr/lib64/ocaml/inotify/META
/usr/lib64/ocaml/inotify/inotify.a
/usr/lib64/ocaml/inotify/inotify.cma
/usr/lib64/ocaml/inotify/inotify.cmi
/usr/lib64/ocaml/inotify/inotify.cmxa
/usr/lib64/ocaml/inotify/inotify.mli
/usr/lib64/ocaml/inotify/inotify.cmx
/usr/lib64/ocaml/inotify/inotify.annot
/usr/lib64/ocaml/inotify/inotify.cmt
/usr/lib64/ocaml/inotify/inotify.cmti
/usr/lib64/ocaml/inotify/inotify.cmxs
/usr/lib64/ocaml/inotify/libinotify_stubs.a
/usr/lib64/ocaml/stublibs/dllinotify_stubs.so
/usr/lib64/ocaml/stublibs/dllinotify_stubs.so.owner
%doc /usr/share/doc/*

%description
OCAML bindings for inotify
