# Script generated with Bloom
pkgdesc="ROS - The `pr2_mechanism_diagnostics` node subscribes to `mechanism_statistics` and publishes diagnostics data for joints and controllers on `/diagnostics`."
url='http://ros.org/wiki/pr2_mechanism_diagnostics'

pkgname='ros-kinetic-pr2-mechanism-diagnostics'
pkgver='1.8.17_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-angles'
'ros-kinetic-catkin'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-pr2-mechanism-model'
'ros-kinetic-pr2-mechanism-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-rostest'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-urdf'
)

depends=('ros-kinetic-angles'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-pr2-mechanism-model'
'ros-kinetic-pr2-mechanism-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-urdf'
)

conflicts=()
replaces=()

_dir=pr2_mechanism_diagnostics
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_mechanism_diagnostics $srcdir/pr2_mechanism_diagnostics
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

